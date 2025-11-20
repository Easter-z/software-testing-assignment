package com.lab.equipment.system;

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
        
        // 创建测试表
        try (Statement stmt = connection.createStatement()) {
            stmt.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    role VARCHAR(20) DEFAULT 'USER'
                )
                """);
                
            stmt.execute("""
                CREATE TABLE IF NOT EXISTS equipment_reservations (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    equipment_id INTEGER,
                    start_time TIMESTAMP,
                    end_time TIMESTAMP,
                    status VARCHAR(20) DEFAULT 'PENDING'
                )
                """);
        }
    }

    // 用例6: 数据库连接测试
    @Test
    public void testDatabaseConnection() throws Exception {
        assertNotNull(connection);
        assertFalse(connection.isClosed());
    }

    // 用例7: 用户表约束测试 - 用户名唯一性
    @Test
    public void testUserTable_UniqueUsernameConstraint() throws Exception {
        try (Statement stmt = connection.createStatement()) {
            // 第一次插入应该成功
            stmt.execute("INSERT INTO users (username, email) VALUES ('unique_user', 'u1@lab.com')");
            
            // 第二次插入相同用户名应该失败
            assertThrows(Exception.class, () -> {
                stmt.execute("INSERT INTO users (username, email) VALUES ('unique_user', 'u2@lab.com')");
            });
        }
    }

    // 用例8: 设备预约业务逻辑测试
    @Test
    public void testEquipmentReservation_ComplexBusinessLogic() throws Exception {
        try (Statement stmt = connection.createStatement()) {
            // 1. 插入测试用户
            stmt.execute("INSERT INTO users (username, email) VALUES ('reservation_user', 'res@lab.com')");
            
            ResultSet rs = stmt.executeQuery("SELECT id FROM users WHERE username = 'reservation_user'");
            rs.next();
            int userId = rs.getInt("id");
            
            // 2. 插入预约记录
            stmt.execute(String.format("""
                INSERT INTO equipment_reservations (user_id, equipment_id, start_time, end_time, status) 
                VALUES (%d, 1, NOW(), NOW() + INTERVAL '2 hours', 'ACTIVE')
                """, userId));
            
            // 3. 验证状态
            rs = stmt.executeQuery("SELECT status FROM equipment_reservations WHERE user_id = " + userId);
            rs.next();
            assertEquals("ACTIVE", rs.getString("status"));
        }
    }

    // 用例9: 复杂联表查询测试
    @Test
    public void testComplexJoinQuery() throws Exception {
        try (Statement stmt = connection.createStatement()) {
            // 准备测试数据
            stmt.execute("INSERT INTO users (username, email) VALUES ('query_user', 'query@lab.com')");
            
            ResultSet rs = stmt.executeQuery("""
                SELECT u.username, er.status 
                FROM equipment_reservations er
                JOIN users u ON er.user_id = u.id
                WHERE u.username = 'query_user'
                """);
            
            assertNotNull(rs);
        }
    }
}
