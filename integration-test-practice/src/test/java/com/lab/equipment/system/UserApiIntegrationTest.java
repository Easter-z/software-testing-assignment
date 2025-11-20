package com.lab.equipment.system;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class UserApiIntegrationTest {

    @BeforeEach
    public void setUp() {
        RestAssured.baseURI = "http://localhost:8080/api/v1";
    }

    // 用例1: 创建用户 - 成功
    @Test
    public void testCreateUser_Success() {
        given()
            .contentType(ContentType.JSON)
            .body("""
                {
                    "username": "testuser",
                    "email": "test@lab.com",
                    "role": "RESEARCHER"
                }
                """)
        .when()
            .post("/users")
        .then()
            .statusCode(201)
            .body("id", notNullValue())
            .body("username", equalTo("testuser"));
    }

    // 用例2: 创建用户 - 邮箱格式错误
    @Test
    public void testCreateUser_InvalidEmail() {
        given()
            .contentType(ContentType.JSON)
            .body("{\"username\": \"user\", \"email\": \"invalid-email\"}")
        .when()
            .post("/users")
        .then()
            .statusCode(400)
            .body("error", containsString("邮箱格式不正确"));
    }

    // 用例3: 查询用户列表 - 分页参数验证
    @Test
    public void testGetUsers_WithPagination() {
        given()
            .param("page", 0)
            .param("size", 10)
        .when()
            .get("/users")
        .then()
            .statusCode(200)
            .body("content", not(empty()))
            .body("totalPages", greaterThan(0));
    }

    // 用例4: 获取特定用户详情
    @Test
    public void testGetUserById_Success() {
        String userId = "user-123";
        
        when()
            .get("/users/{id}", userId)
        .then()
            .statusCode(200)
            .body("id", equalTo(userId))
            .body("username", notNullValue());
    }

    // 用例5: 更新用户信息
    @Test
    public void testUpdateUser_Success() {
        String userId = "user-123";
        
        given()
            .contentType(ContentType.JSON)
            .body("{\"email\": \"updated@lab.com\"}")
        .when()
            .patch("/users/{id}", userId)
        .then()
            .statusCode(200)
            .body("email", equalTo("updated@lab.com"));
    }
}
