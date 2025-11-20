import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;
import static org.junit.jupiter.api.Assertions.*;

public class MicroserviceIntegrationTest {

    @BeforeEach
    public void setUp() {
        RestAssured.baseURI = "http://localhost:8080";
    }

    @Test
    public void testUserEquipmentAccess_Integration() {
        given()
            .contentType(ContentType.JSON)
            .body("{\"username\": \"researcher\", \"role\": \"RESEARCHER\"}")
        .when()
            .post("/users")
        .then()
            .statusCode(201);

        given()
            .param("userId", "researcher")
            .param("equipmentId", "microscope")
        .when()
            .get("/access/check")
        .then()
            .statusCode(200);
    }

    @Test 
    public void testCompleteReservationFlow() {
        String userId = given()
            .contentType(ContentType.JSON)
            .body("{\"username\": \"researcher\", \"email\": \"res@lab.com\"}")
        .when()
            .post("/users")
        .then()
            .statusCode(201)
            .extract().jsonPath().getString("id");

        given()
            .contentType(ContentType.JSON)
            .body("{\"userId\": \"" + userId + "\", \"equipmentId\": \"device1\"}")
        .when()
            .post("/reservations")
        .then()
            .statusCode(201);
    }

    @Test
    public void testServiceDegradation() {
        given()
        .when()
            .get("/equipment/unavailable-service")
        .then()
            .statusCode(503);
    }

    @Test
    public void testHealthCheck() {
        given()
        .when()
            .get("/health")
        .then()
            .statusCode(200);
    }
}
