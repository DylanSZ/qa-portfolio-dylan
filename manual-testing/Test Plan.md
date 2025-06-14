# Login Page – Test Plan

This test plan outlines the objectives, scope, strategy, and scenarios for testing the login functionality of the application.

---

## Objective

To verify the functionality, usability, security, and compatibility of the login page to ensure only authorized users can access the system.

---

## Scope

### In Scope:
- Functional testing
- UI/UX validation
- Client-side and server-side validation
- Security validations (basic)

### Out of Scope:
- Social login (e.g., Google/Facebook)
- Password recovery flows (covered in separate test)

---

## Test Strategy

| Type of Testing         | Tools/Methods Used                         |
|-------------------------|--------------------------------------------|
| Functional Testing      | Manual Testing using Browser               |
| UI/UX Testing           | Manual Testing + UI checklist              |
| Security Testing        | Input validation (e.g., SQL injection)     |
| Compatibility Testing   | Cross-browser + Mobile device checks       |
| Regression Testing      | Re-run existing test cases after changes   |

---

## Test Roles & Responsibility

| Role                 | Responsibility                                     |
|----------------------|----------------------------------------------------|
| QA Engineer          | Prepare test plan, design test cases, execute tests |
| QA Lead              | Review plan, assign tasks, and ensure coverage     |

---

## Features to Test

### Functional Scenarios
**Positive Test Cases:**
- Login with valid username and password.
- Login with special characters allowed in username (e.g., dot, underscore).

**Negative Test Cases:**
- Login with incorrect password.
- Login with unregistered username.
- Attempt login with blank username or password fields.

### UI/UX Scenarios
7. Login button visibility and state (enabled/disabled)
8. Placeholder text in input fields
9. Font size, spacing, alignment consistency
10. Focus moves correctly when tab key is used

### Compatibility Scenarios
11. Login page on mobile browsers (Chrome, Safari)
12. Responsive layout on tablet and desktop
13. Cross-browser test (Chrome, Edge, Firefox)

### Security Scenarios
14. SQL injection prevention
15. HTML/JS injection blocked in input
16. Session cookie should be secure and HttpOnly

---

## ⏱️ Test Schedule

| Phase               | Timeline        |
|---------------------|-----------------|
| Test Planning       | 1 day           |
| Test Case Design    | 1 day           |
| Test Execution      | 2 days          |
| Bug Reporting & Retest | As needed     |

---

## ✅ Entry and Exit Criteria

**Entry Criteria**
- Development of login feature is complete
- Test environment is set up and accessible
- Jira requirements/user stories are reviewed

**Exit Criteria**
- All critical and high-severity bugs are resolved
- All test cases (manual/automated) are executed
- All regressions have been retested

---

## 📁 Deliverables

- Test Plan
- Test Cases
- Bug Reports (in Jira)
- Test Summary Report

---

**Prepared By**: `Dylan`  
**Last Updated**: `11 May 2025`  

