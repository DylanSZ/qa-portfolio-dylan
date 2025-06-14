# ✅ Login Page – Test Cases

This document outlines detailed test cases for validating the login functionality, including positive, negative, UI/UX, compatibility, and security scenarios.

---

## 🔐 Functional Test Cases

### 1. User should successfully log in with valid username and password
- **Test Steps:**
  1. Navigate to the login page.
  2. Enter a valid username.
  3. Enter the correct password.
  4. Click the "Login" button.
- **Expected Result:** User is redirected to the dashboard or homepage.
- **Test Result:** _Pass / Fail_

---

### 2. System should display error when incorrect password is entered
- **Test Steps:**
  1. Navigate to the login page.
  2. Enter a valid username.
  3. Enter an incorrect password.
  4. Click "Login".
- **Expected Result:** Error message "Incorrect password" is shown.
- **Test Result:** _Pass / Fail_

---

### 3. Login form should show validation errors when both fields are blank
- **Test Steps:**
  1. Navigate to login page.
  2. Leave username and password empty.
  3. Click "Login".
- **Expected Result:** Validation messages "Username is required" and "Password is required" are displayed.
- **Test Result:** _Pass / Fail_

---

### 4. Login attempt with unregistered username should fail with error
- **Test Steps:**
  1. Enter a username that doesn't exist.
  2. Enter any password.
  3. Click "Login".
- **Expected Result:** Error message "User not found" or equivalent.
- **Test Result:** _Pass / Fail_

---

### 5. System should validate individual field when only username is entered
- **Test Steps:**
  1. Enter a valid username.
  2. Leave password blank.
  3. Click "Login".
- **Expected Result:** Validation message "Password is required" is displayed.
- **Test Result:** _Pass / Fail_

---

## 🎨 UI/UX Test Cases

### 6. Login button should be disabled when required fields are empty
- **Test Steps:**
  1. Leave both fields blank.
  2. Observe the state of the Login button.
- **Expected Result:** Login button is disabled or inactive.
- **Test Result:** _Pass / Fail_

---

### 7. Placeholder text should be visible in username and password fields
- **Test Steps:**
  1. Navigate to login page.
  2. Check input placeholders.
- **Expected Result:** "Enter Username" and "Enter Password" placeholders are shown.
- **Test Result:** _Pass / Fail_

---

### 8. Focus should move correctly using tab key
- **Test Steps:**
  1. Press "Tab" on username field.
- **Expected Result:** Cursor moves to password, then to Login button.
- **Test Result:** _Pass / Fail_

---

## 📱 Compatibility Test Cases

### 9. Login form layout should be responsive on tablet screen
- **Test Steps:**
  1. Open login page on a tablet browser.
- **Expected Result:** Form adjusts properly without UI breaks.
- **Test Result:** _Pass / Fail_

### 10. Login form should display correctly across major browsers
- **Test Steps:**
  1. Open login page on Chrome, Firefox, Edge.
- **Expected Result:** Consistent layout and functionality.
- **Test Result:** _Pass / Fail_

---

## 🔒 Security Test Cases

### 11. Application should block SQL injection in input fields
- **Test Steps:**
  1. Enter `admin' OR '1'='1` in the username field.
  2. Enter any password.
- **Expected Result:** Login fails with a generic error, no SQL exposed.
- **Test Result:** _Pass / Fail_

---

### 12. HTML or JS script input should be blocked
- **Test Steps:**
  1. Enter `<script>alert(1)</script>` in either field.
- **Expected Result:** Script is neutralized; no code executes.
- **Test Result:** _Pass / Fail_

---

### 13. Session cookie should have Secure and HttpOnly flags
- **Test Steps:**
  1. Inspect browser cookies after login.
- **Expected Result:** Session cookies have `Secure` and `HttpOnly` attributes.
- **Test Result:** _Pass / Fail_

---

**Prepared by:** `Dylan`  
**Last Updated:** `11 May 2025`
