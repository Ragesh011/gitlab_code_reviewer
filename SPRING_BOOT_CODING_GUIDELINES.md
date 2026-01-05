# Spring Boot Coding Guidelines & Review Checklist

This document outlines global rules, best practices, and coding standards for Java Spring Boot applications. It combines general Java clean code principles with specific Spring Boot conventions. These guidelines are intended for use by generative AI models and human reviewers to ensure code quality, security, and maintainability.

## 1. General Java Best Practices

### Readability & Naming
*   **Clarity**: Ensure code is easy to understand.
*   **Classes**: Use **PascalCase**. Must be nouns (e.g., `OrderService`).
*   **Methods**: Use **camelCase**. Must be verbs indicating action (e.g., `calculateTotal`).
*   **Variables**: Use **camelCase**. Avoid single letters unless in short loops.
*   **Constants**: Use **SCREAMING_SNAKE_CASE** (e.g., `MAX_RETRY_COUNT`).
*   **No Magic Values**: Avoid hardcoded numbers or strings. Use constants or enums. Skip checks on enum classes and test packages

### formatting & Style
*   **Consistency**: Maintain consistent indentation and line lengths.
*   **Tools**: Enforce standards automatically using static analysis tools like **SonarQube** or **Checkstyle**.
*   **Imports**: Remove all **unused imports**. Auto-organize imports.

### Error Prevention & Performance
*   **Null Safety**: Avoid `NullPointerException`. Use **`Optional`** or perform explicit null checks. **Exception**: This rule does not apply to **Enum** classes.
*   **Boolean Checks**: When checking non-primitive `Boolean` values, use `BooleanUtils.isTrue(value)` instead of direct access to avoid NPEs (e.g., `if(BooleanUtils.isTrue(applicant.getIsActive()))`).
*   **String Manipulation**: Use `StringBuilder` for string concatenation inside loops to optimize performance.
*   **Duplication (DRY)**: Refactor repetitive code into reusable methods or utility classes.

### Modularity & Design Principles
*   **Single Responsibility (SRP)**: Each class/method should have exactly one purpose.
*   **Composition over Inheritance**: Prefer composition to reduce coupling.
*   **Interfaces**: Code to interfaces (e.g., `List` instead of `ArrayList`), not implementations.

## 2. Spring Boot Architecture & Configuration

### Project Structure
*   **Main Class**: explicit location in the root package to ensure correct component scanning (`@SpringBootApplication`).
*   **Layered Architecture**: Strict separation of concerns:
    *   **Controller**: Handles HTTP requests/responses.
    *   **Service**: Contains all business logic.
    *   **Repository**: Manages data access.

### Configuration Management
*   **Externalization**: Move environment-specific configs (DB creds, API keys) to `application.properties`, `application.yml`, or secure vaults.
*   **Security**: **NEVER** hardcode sensitive data (passwords, PII) in source code.
*   **Profiles**: Use `@Profile` annotations to define environment-specific beans (e.g., dev vs. prod).

## 3. REST API Best Practices

*   **Naming**: Use consistent, plural resource names (e.g., `/api/v1/customers/{id}`).
*   **DTOs**: **Always** use Data Transfer Objects. **Never** expose JPA entities directly to clients.
*   **Validation**: Validate inputs using `@Valid` and Bean Validation annotations (`@NotNull`, `@Email`).
*   **Status Codes**: Return appropriate HTTP status codes:
    *   `200 OK`: Success.
    *   `201 Created`: Resource successfully created.
    *   `400 Bad Request`: Validation errors.
    *   `404 Not Found`: Resource does not exist.
    *   `500 Internal Server Error`: Generic handling.

## 4. Service Layer & Data Access (JPA)

*   **Placement**: Business logic belongs in the **Service** layer, not Controllers or Repositories.
*   **Transactions**:
    *   Use `@Transactional` on service methods modifying data.
    *   Use `@Transactional(readOnly = true)` for read operations to optimize performance.
*   **Performance**:
    *   **Lazy Loading**: Ensure associations use `FetchType.LAZY` defaults to avoid N+1 query problems.
    *   **Pagination**: Use `Pageable` for fetching large datasets.
*   **Injection**: Use **Constructor Injection** (`final` fields) instead of `@Autowired` on fields.
*   **Audit Fields**: Fields like `created_at` and `updated_at` should **not** exist directly in classes annotated with `@Entity`.

## 5. Error Handling, Logging & Security

*   **Global Handling**: Use `@ControllerAdvice` for centralized exception handling to ensure consistent JSON error responses.
*   **Logging**:
    *   Use **SLF4J** with Logback. Avoid `System.out.println()`.
    *   **Mandatory Service Logging**: Service layer methods should have **at least one** log message.
    *   Do **not** log sensitive information (passwords, PII).
*   **Security**:
    *   Verify **Spring Security** configuration.
    *   Sanitize inputs to prevent **SQL Injection** and **XSS**.

## 6. Review Checklist for AI Model

When reviewing a Merge Request, verify the following:

### General & Style
- [ ] Are naming conventions (PascalCase, camelCase) followed?
- [ ] Are unused imports removed?
- [ ] Is code properly formatted with no hardcoded magic values (skip enum classes and test packages)?
- [ ] Is `Optional` used to handle nulls safely (skip Enums)?
- [ ] Is `BooleanUtils.isTrue()` used for nullable Boolean conditions?
- [ ] Is `StringBuilder` used for loop concatenations?

### Architecture
- [ ] Is the Main class in the root package?
- [ ] Are Controllers thin and Services stateless?
- [ ] Is Constructor Injection used?

### REST & DTOs
- [ ] Are DTOs used for all requests/responses?
- [ ] Is input validation (`@Valid`) present?
- [ ] Are HTTP status codes correct (201, 404, etc.)?

### Data Access & Performance
- [ ] Is business logic isolated in the Service layer?
- [ ] Do entities avoid directly defining `created_at`/`updated_at`?
- [ ] Is `@Transactional(readOnly = true)` used for reads?
- [ ] Are associations Lazy loaded?
- [ ] Is pagination used for lists?

### Security & Testing
- [ ] Are secrets excluded from code?
- [ ] Do service methods have at least one log statement?
- [ ] Is Spring Security configured correctly?
- [ ] Are unit/integration tests present for new code?
