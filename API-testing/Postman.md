# ✅ Postman API Test – `masterBankEntries` Validation

This document showcases a sample test script created using **Postman** to validate the API response for the `masterBankEntries` endpoint. It demonstrates best practices in status code validation, response structure checks, type assertions, and data rules.

---

## 🔍 Overview

This test suite ensures that:

- The response is fast and successful.
- The returned data (`masterBankEntries`) is a valid and well-structured array.
- All expected fields are present and conform to specific formats and values.
- The dataset follows business rules like uniqueness and type validation.

---

## 🧪 Test Coverage

| No.   | Test Case Description                                                              |
|-------|-------------------------------------------------------------------------------------|
| TC001 | Status code should be `200`                                                        |
| TC002 | Response time should be under `1000ms`                                             |
| TC003 | `errorCode` should equal `0`                                                       |
| TC004 | `masterBankEntries` should be a non-empty array                                    |
| TC005 | Each entry should have valid `bank_Name`, `bank_Full_Name`, `payment_Type`, etc.  |
| TC006 | `payment_Type` must be one of: `Maybank`, `CIMB`, `DBS`, `BCA`                |
| TC007 | All `bank_Name` values should be unique                                            |

---

## 💻 Postman Test Script

```javascript
const jsonData = pm.response.json();
const entries = jsonData?.data?.masterBankEntries || [];

// Basic checks
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response time is under 1000ms", function () {
  pm.expect(pm.response.responseTime).to.be.below(1000);
});

pm.test("Error code is 0", function () {
  pm.expect(jsonData.errorCode).to.eql(0);
});

// Array validation
pm.test("masterBankEntries array exists and is not empty", function () {
  pm.expect(entries, "masterBankEntries should be a non-empty array").to.be.an('array').that.is.not.empty;
});

// Field validation for each entry
pm.test("Validate fields in each entry", function () {
  entries.forEach((entry, index) => {
    pm.expect(entry, `Entry at index ${index} is missing bank_Name`).to.have.property("bank_Name").that.is.a("string");
    pm.expect(entry, `Entry at index ${index} is missing bank_Full_Name`).to.have.property("bank_Full_Name").that.is.a("string");
    pm.expect(entry, `Entry at index ${index} is missing payment_Type`).to.have.property("payment_Type").that.is.a("string");
    pm.expect(entry, `Entry at index ${index} is missing status`).to.have.property("status").that.is.a("boolean");

    pm.expect(entry, `Entry at index ${index} is missing min_Digit`).to.have.property("min_Digit").that.is.a("number");
    pm.expect(Number.isInteger(entry.min_Digit), `min_Digit must be an integer at index ${index}`).to.be.true;

    pm.expect(entry, `Entry at index ${index} is missing max_Digit`).to.have.property("max_Digit").that.is.a("number");
    pm.expect(Number.isInteger(entry.max_Digit), `max_Digit must be an integer at index ${index}`).to.be.true;
  });
});

// Validate allowed payment types
const allowedTypes = ["Maybank", "CIMB", "DBS", "BCA"];
pm.test("Validate payment_Type values", function () {
  entries.forEach((entry, index) => {
    pm.expect(allowedTypes, `Invalid payment_Type at index ${index}: ${entry.payment_Type}`).to.include(entry.payment_Type);
  });
});

// Check for uniqueness of bank_Name
const bankNames = entries.map(e => e.bank_Name);
const uniqueNames = [...new Set(bankNames)];

pm.test("bank_Name values are unique", function () {
  pm.expect(bankNames.length, "bank_Name values should be unique").to.eql(uniqueNames.length);
});
