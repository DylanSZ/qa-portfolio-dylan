## 🧪 Test Scenarios for Login Page

| Scenario ID | Test Scenario Description                                           | Type         |
|-------------|---------------------------------------------------------------------|--------------|
| TS-01       | Verify login with valid username and password                      | Positive     |
| TS-02       | Verify login with invalid username and/or password                 | Negative     |
| TS-03       | Verify login attempt with empty username and password fields       | Negative     |
| TS-04       | Verify login attempt with only username filled                     | Negative     |
| TS-05       | Verify login attempt with only password filled                     | Negative     |
| TS-06       | Verify password field is masked                                    | Functional   |
| TS-07       | Verify the login button is disabled until both fields are filled   | UI/UX        |
| TS-08       | Verify placeholder text is shown in input fields                   | UI/UX        |
| TS-09       | Verify login page layout on different screen sizes (responsive)    | Compatibility|
| TS-10       | Verify login page works on major browsers (Chrome, Firefox, Edge)  | Compatibility|
| TS-11       | Verify SQL injection does not bypass login authentication          | Security     |
| TS-12       | Verify HTML/JS injection is blocked in input fields                | Security     |
| TS-13       | Verify session cookies are marked as Secure and HttpOnly           | Security     |
| TS-14       | Verify keyboard navigation and tab order between input fields      | Accessibility|

