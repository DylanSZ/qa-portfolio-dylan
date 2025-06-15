# Test Scenarios – Login Page

This document outlines the high-level test scenarios identified for validating the functionality, usability, compatibility, and security of the login page.

---

## Functional Test Scenarios

- **TS001**: Verify login functionality with valid username and password.
- **TS002**: Verify login with valid username containing special characters (e.g., dot, underscore).
- **TS003**: Verify login with incorrect password.
- **TS004**: Verify login with an unregistered username.
- **TS005**: Verify login behavior when username and/or password fields are left empty.

---

## UI/UX Test Scenarios

- **TS006**: Verify that the login button is appropriately enabled or disabled based on field input.
- **TS007**: Verify placeholder text for username and password input fields.
- **TS008**: Verify consistency in font size, alignment, and spacing on the login page.
- **TS009**: Verify keyboard navigation and tab order across login fields.

---

## Compatibility Test Scenarios

- **TS010**: Verify the login page functionality and layout on mobile browsers (e.g., Chrome, Safari).
- **TS011**: Verify responsive layout behavior across desktop and tablet resolutions.
- **TS012**: Verify cross-browser compatibility on modern browsers (Chrome, Firefox, Edge).

---

## Security Test Scenarios

- **TS013**: Verify that the system prevents SQL injection via input fields.
- **TS014**: Verify that HTML or JavaScript code injection is blocked and safely handled.
- **TS015**: Verify that session cookies are configured with `Secure` and `HttpOnly` attributes.

---

**Document Prepared By**: `Dylan`  
**Last Reviewed**: `11 May 2025`
