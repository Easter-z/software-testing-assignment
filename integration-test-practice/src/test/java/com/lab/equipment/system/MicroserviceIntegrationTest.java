package com.lab.equipment.system;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.List;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;
import static org.junit.jupiter.api.Assertions.*;

public class MicroserviceIntegrationTest {

    private final String USER_SERVICE_URL = "http://localhost:8081";
    private final String EQUIPMENT_SERVICE_URL = "http://localhost:8082"; 
    private final String RESERVATION_SERVICE_URL = "http://localhost:8083";

    @BeforeEach
    public void setUp() {
        // 设置基础URI，实际测试中需要根据环境调整
        RestAssured.baseURI = "http://localhost:8080";
    }

    // 用例11: 用户服务与设备服务集成 - 验证用户权限
    @Test
    public void testUserEquipmentAccess_Integration() {
        given()
            .contentType(ContentType.JSON)
            .body("""
                {
                    "username": "researcher",
                    "role": "RESEARCHER"
                }
                """)
        .when()
            .post("/users")
        .then()
            .statusCode(201);

        given()
            .param("userId", "researcher")
            .param("equipmentId", "advanced-microscope")
        .when()
            .get("/access/check")
        .then()
            .statusCode(200)
            .body("hasAccess", equalTo(true));
    }

    // 用例12: 完整的设备预约流程测试
    @Test 
    public void testCompleteReservationFlow() {
        // 1. 创建用户
        String userId = given()
            .contentType(ContentType.JSON)
            .body("""
                {
                    "username": "test_researcher",
                    "email": "researcher@lab.com",
                    "role": "RESEARCHER"
                }
                """)
        .when()
            .post("/users")
        .then()
            .statusCode(201)
            .extract().jsonPath().getString("id");

        // 2. 查询可用设备
        List<String> availableEquipment = given()
            .param("startTime", "2024-01-20T10:00:00")
            .param("endTime", "2024-01-20T12:00:00")
        .when()
            .get("/equipment/available")
        .then()
            .statusCode(200)
            .extract().jsonPath().getList("id");

        assertFalse(availableEquipment.isEmpty());

        // 3. 创建预约
        String equipmentId = availableEquipment.get(0);
        String reservationId = given()
            .contentType(ContentType.JSON)
            .body(String.format("""
                {
                    "userId": "%s",
                    "equipmentId": "%s",
                    "startTime": "2024-01-20T10:00:00", 
                    "endTime": "2024-01-20T12:00:00"
                }
                """, userId, equipmentId))
        .when()
            .post("/reservations")
        .then()
            .statusCode(201)
            .extract().jsonPath().getString("id");

        // 4. 验证预约状态
        given()
        .when()
            .get("/reservations/{id}", reservationId)
        .then()
            .statusCode(200)
            .body("status", equalTo("CONFIRMED"));
    }

    // 用例13: 服务降级测试
    @Test
    public void testServiceDegradation() {
        given()
        .when()
            .get("/equipment/unavailable-service")
        .then()
            .statusCode(503)
            .body("fallback", equalTo(true));
    }
}
