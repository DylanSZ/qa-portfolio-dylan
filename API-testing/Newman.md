
## Overview

This section highlights the integration of **Postman** and **Newman** for API testing, focusing on command-line execution and automated HTML report generation. The objective is to showcase efficient, repeatable, and sharable API test executions as part of the QA workflow.

---

## Key Achievement

Successfully introduced **Newman** to the QA team for running Postman collections via the command line. This enabled:
- Automated generation of detailed HTML reports
- Easier test result sharing across teams

---

## Newman Execution in Command Line

```bash
newman run my-collection.json -e my-environment.json -r cli,html --reporter-html-export report.html
```

📸 **Screenshot – Running Newman via CLI:**

![Running Newman](https://github.com/user-attachments/assets/9defb6f9-cbb8-449f-ab43-4501daca5236)

---

## HTML Report Generated by Newman

The generated HTML report provides clear insights into the request execution status, response time, and failure points if any.

📸 **Screenshot – Newman HTML Report:**

![Newman HTML Report](https://github.com/user-attachments/assets/a474992c-94c2-4d70-9f8a-63761c97bee3)



---

## Tools Used
- **Postman**: API request building and test scripting
- **Newman**: CLI execution of Postman collections
- **HTML Reporter**: Plugin to generate clean test result visualizations

---

This setup reflects real-world practices for automating API tests in continuous integration pipelines and improving test transparency for all stakeholders.
