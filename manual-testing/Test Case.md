# ✅ Test Cases – Login Page

This document contains the detailed test cases that correspond to the defined test scenarios for the login page.

---

### TC001 – Login with Valid Credentials

- **Scenario ID**: TS001  
- **Test Steps**:
  1. Navigate to the login page.
  2. Enter a valid username and password.
  3. Click the "Login" button.  
- **Expected Result**: User is successfully logged in and redirected to the dashboard.

---

### TC002 – Login with Special Characters in Username

- **Scenario ID**: TS002  
- **Test Steps**:
  1. Enter a username containing allowed special characters (e.g., john.doe).
  2. Enter a valid password.
  3. Click the "Login" button.  
- **Expected Result**: Login succeeds and user is redirected appropriately.

---

### TC003 – Login with Incorrect Password

- **Scenario ID**: TS003  
- **Test Steps**:
  1. Enter a valid username.
  2. Enter an incorrect password.
  3. Click the "Login" button.  
- **Expected Result**: System displays an error message: "Invalid username or password."

---

### TC004 – Login with Unregistered Username

- **Scenario ID**: TS004  
- **Test Steps**:
  1. Enter a username not registered in the system.
  2. Enter a valid or invalid password.
  3. Click the "Login" button.  
- **Expected Result**: System denies login and displays an appropriate error message.

---

### TC005 – Login with Empty Fields

- **Scenario ID**: TS005  
- **Test Steps**:
  1. Leave both username and password fields empty.
  2. Click the "Login" button.  
- **Expected Result**: System displays validation messages for both required fields.

---

### TC006 – Login Button State

- **Scenario ID**: TS006  
- **Test Steps**:
  1. Observe the login button state before and after entering values in input fields.  
- **Expected Result**: The button is enabled only when both username and password fields are populated.

---

### TC007 – Placeholder Text Verification

- **Scenario ID**: TS007  
- **Test Steps**:
  1. View the login page.
  2. Check placeholder text in username and password fields.  
- **Expected Result**: Placeholder text (e.g., “Enter your username”) is clearly displayed.

---

### TC008 – UI Layout Consistency

- **Scenario ID**: TS008  
- **Test Steps**:
  1. Observe the layout, alignment, spacing, and fonts used in the login form.  
- **Expected Result**: UI elements should follow the defined design guidelines.

---

### TC009 – Keyboard Navigation Order

- **Scenario ID**: TS009  
- **Test Steps**:
  1. Use the Tab key to move between fields.  
- **Expected Result**: Focus moves from username → password → login button in order.

---

### TC010 – Mobile Browser Compatibility

- **Scenario ID**: TS010  
- **Test Steps**:
  1. Open the login page in mobile browsers (e.g., Chrome, Safari).  
- **Expected Result**: The page should be fully functional and properly displayed on mobile.

---

### TC011 – Responsive Layout on Devices

- **Scenario ID**: TS011  
- **Test Steps**:
  1. Resize the browser or test on tablet/desktop.  
- **Expected Result**: The layout should adjust and display correctly based on screen size.

---

### TC012 – Cross-Browser Functionality

- **Scenario ID**: TS012  
- **Test Steps**:
  1. Open the login page on Chrome, Firefox, and Edge browsers.  
- **Expected Result**: Page functions consistently across all browsers.

---

### TC013 – SQL Injection Attempt

- **Scenario ID**: TS013  
- **Test Steps**:
  1. Enter `' OR '1'='1` in the username field.
  2. Enter any password.
  3. Attempt to log in.  
- **Expected Result**: Login fails and input is sanitized. No data leakage or unauthorized access.

---

### TC014 – JavaScript Injection Handling

- **Scenario ID**: TS014  
- **Test Steps**:
  1. Enter `<script>alert('xss')</script>` in the username field.  
- **Expected Result**: Input is treated as plain text. No script is executed.

---

### TC015 – Secure Session Cookie Validation

- **Scenario ID**: TS015  
- **Test Steps**:
  1. Successfully log in.
  2. Inspect session cookie attributes in developer tools.  
- **Expected Result**: `Secure` and `HttpOnly` flags are set on session cookies.

---

**Document Prepared By**: `Dylan`  
**Last Reviewed**: `11 May 2025`
