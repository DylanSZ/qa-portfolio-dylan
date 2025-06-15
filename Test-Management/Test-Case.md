# Login Page – Test Cases

This document contains detailed manual test cases derived from the Login Page Test Scenarios.

---

## Functional Test Cases

### TC001 – Login succeeds with valid credentials  
**Scenario ID:** TS001  
**Test Steps:**
1. Navigate to the login page.
2. Enter a registered username and correct password.
3. Click the "Login" button.  
**Expected Result:** User is successfully logged in and redirected to the dashboard.  
**Test Result:** _Pass / Fail_

---

### TC002 – Login succeeds with special characters in username  
**Scenario ID:** TS002  
**Test Steps:**
1. Navigate to the login page.
2. Enter a valid username containing special characters (e.g., `john.doe_99`).
3. Enter the correct password.
4. Click "Login".  
**Expected Result:** User is successfully logged in without errors.  
**Test Result:** _Pass / Fail_

---

### TC003 – Login fails with incorrect password  
**Scenario ID:** TS003  
**Test Steps:**
1. Enter valid username.
2. Enter incorrect password.
3. Click "Login".  
**Expected Result:** Login fails with error message: “Incorrect username or password.”  
**Test Result:** _Pass / Fail_

---

### TC004 – Login fails with unregistered username  
**Scenario ID:** TS004  
**Test Steps:**
1. Enter an unregistered username.
2. Enter any password.
3. Click "Login".  
**Expected Result:** Login fails with error message: “Incorrect username or password.”  
**Test Result:** _Pass / Fail_

---

### TC005 – Login fails when fields are left blank  
**Scenario ID:** TS005  
**Test Steps:**
1. Leave both username and password fields empty.
2. Click "Login".  
**Expected Result:** Validation messages: “Username is required.” and “Password is required.”  
**Test Result:** _Pass / Fail_

---

## UI/UX Test Cases

### TC006 – Login button enabled only when required fields are filled  
**Scenario ID:** TS006  
**Test Steps:**
1. Open login page.
2. Leave fields blank – Login button should be disabled.
3. Fill in both username and password – Button should become enabled.  
**Expected Result:** Button behaves as per field state.  
**Test Result:** _Pass / Fail_

---

### TC007 – Placeholder text is present in input fields  
**Scenario ID:** TS007  
**Test Steps:**
1. Open login page.
2. Observe input fields before typing.  
**Expected Result:** Username field shows “Enter your username”; password field shows “Enter your password”.  
**Test Result:** _Pass / Fail_

---

### TC008 – Font and layout consistency on login page  
**Scenario ID:** TS008  
**Test Steps:**
1. Inspect font style, spacing, and alignment of all UI elements.  
**Expected Result:** Font and spacing are consistent and aligned as per design specs.  
**Test Result:** _Pass / Fail_

---

### TC009 – Keyboard tab navigation follows logical order  
**Scenario ID:** TS009  
**Test Steps:**
1. Click username field.
2. Press `Tab` and observe focus flow.  
**Expected Result:** Cursor moves from username → password → login button.  
**Test Result:** _Pass / Fail_

---

## Compatibility Test Cases

### TC010 – Mobile browser login functionality  
**Scenario ID:** TS010  
**Test Steps:**
1. Open login page on mobile Chrome or Safari.
2. Attempt login with valid credentials.  
**Expected Result:** Layout is responsive and login works correctly.  
**Test Result:** _Pass / Fail_

---

### TC011 – Layout responsiveness on tablet and desktop  
**Scenario ID:** TS011  
**Test Steps:**
1. Resize browser window or open on tablet.
2. Observe layout and attempt login.  
**Expected Result:** Layout adapts cleanly to all screen sizes.  
**Test Result:** _Pass / Fail_

---

### TC012 – Login on Chrome, Firefox, and Edge  
**Scenario ID:** TS012  
**Test Steps:**
1. Open login page on each browser.
2. Attempt login and inspect layout.  
**Expected Result:** Functionality and UI behave consistently across browsers.  
**Test Result:** _Pass / Fail_

---

## Security Test Cases

### TC013 – SQL injection prevention  
**Scenario ID:** TS013  
**Test Steps:**
1. Enter `' OR '1'='1` in username and any password.
2. Click "Login".  
**Expected Result:** Login fails, and no SQL query manipulation occurs.  
**Test Result:** _Pass / Fa_

