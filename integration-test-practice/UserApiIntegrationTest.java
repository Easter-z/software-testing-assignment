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

    @Test
    public void testCreateUser_Success() {
        given()
            .contentType(ContentType.JSON)
            .body("{\"username\": \"testuser\", \"email\": \"test@lab.com\"}")
        .when()
            .post("/users")
        .then()
            .statusCode(201)
            .body("id", notNullValue());
    }

    @Test
    public void testCreateUser_InvalidEmail() {
        given()
            .contentType(ContentType.JSON)
            .body("{\"username\": \"user\", \"email\": \"invalid-email\"}")
        .when()
            .post("/users")
        .then()
            .statusCode(400);
    }

    @Test
    public void testGetUsers_WithPagination() {
        given()
            .param("page", 0)
            .param("size", 10)
        .when()
            .get("/users")
        .then()
            .statusCode(200);
    }

    @Test
    public void testGetUserById_Success() {
        when()
            .get("/users/user-123")
        .then()
            .statusCode(200);
    }

    @Test
    public void testUpdateUser_Success() {
        given()
            .contentType(ContentType.JSON)
            .body("{\"email\": \"updated@lab.com\"}")
        .when()
            .patch("/users/user-123")
        .then()
            .statusCode(200);
    }
}
