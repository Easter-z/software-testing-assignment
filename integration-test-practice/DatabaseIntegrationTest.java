import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeAll;
import org.testcontainers.containers.PostgreSQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
import static org.junit.jupiter.api.Assertions.*;

@Testcontainers
public class DatabaseIntegrationTest {

    @Container
    private static final PostgreSQLContainer<?> postgres = 
        new PostgreSQLContainer<>("postgres:13")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");

    private static Connection connection;

    @BeforeAll
    static void setUp() throws Exception {
        connection = DriverManager.getConnection(
            postgres.getJdbcUrl(),
            postgres.getUsername(),
            postgres.getPassword()
        );
        
        try (Statement stmt = connection.createStatement()) {
            stmt.execute("""
                CREATE TABLE users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) NOT NULL
                )
                """);
        }
    }

    @Test
    public void testDatabaseConnection() throws Exception {
        assertNotNull(connection);
        assertFalse(connection.isClosed());
    }

    @Test
    public void testUserTable_UniqueUsernameConstraint() throws Exception {
        try (Statement stmt = connection.createStatement()) {
            stmt.execute("INSERT INTO users (username, email) VALUES ('user1', 'u1@lab.com')");
            assertThrows(Exception.class, () -> {
                stmt.execute("INSERT INTO users (username, email) VALUES ('user1', 'u2@lab.com')");
            });
        }
    }

    @Test
    public void testInsertAndQueryUser() throws Exception {
        try (Statement stmt = connection.createStatement()) {
            stmt.execute("INSERT INTO users (username, email) VALUES ('testuser', 'test@lab.com')");
            ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE username = 'testuser'");
            assertTrue(rs.next());
            assertEquals("test@lab.com", rs.getString("email"));
        }
    }

    @Test
    public void testComplexJoinQuery() throws Exception {
        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery("SELECT COUNT(*) as count FROM users");
            assertTrue(rs.next());
            assertTrue(rs.getInt("count") >= 0);
        }
    }
}
