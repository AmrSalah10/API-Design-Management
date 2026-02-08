# 🧼 SOAP Calculator Project

> A hands-on assignment for the **[API Design and Management](https://www.youtube.com/@SoftwareArchTalks)** course on the **Software ArchTalks** YouTube Channel.

![Java](https://img.shields.io/badge/Java-Beginner_Friendly-ED8B00?style=for-the-badge&logo=java&logoColor=white)
![Python](https://img.shields.io/badge/Python-Simple_Client-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SOAP](https://img.shields.io/badge/SOAP-Web_Service-005C84?style=for-the-badge)

## 📖 Overview

This is a simple project that implements a **Calculator SOAP Service** using Java's JAX-WS (Java API for XML Web Services). It follows the **Contract-First** approach, where the service interface is generated from a WSDL (Web Services Description Language) file.

The project consists of two main components:
1.  **Service (Java)**: A standalone SOAP server that exposes an `Add` operation.
2.  **Client (Python)**: A lightweight client script using `zeep` to consume the SOAP service.

This project was built as part of an exploration into **SOAP Services** and **Contract-First Development**, designed to demonstrate practical understanding of XML-based web services.

---

## 🚀 Key Features

-   **Contract-First Design**: Service interface generated directly from `calculator.wsdl`.
-   **Cross-Platform**: Shows how two different programming languages can talk to each other using SOAP.
-   **Standard Compliant**: Uses standard JAX-WS specifications.
-   **Generated Artifacts**: Leveraging `wsimport` for type-safe Java code generation.

---

## 🛠️ Project Structure

```bash
📦 SOAP
 ┣ 📂 Client               # The Python script that asks for the calculation
 ┃ ┣ 📜 main.py           # Runs the client
 ┃ ┗ ...
 ┣ 📂 Service              # The Java server that does the math
 ┃ ┣ 📂 com/calc     # Files created automatically by wsimport
 ┃ ┣ 📜 Main.java         # Starts the server
 ┃ ┗ 📜 calculator.wsdl   # Although this is just a file, it's the "Rule Book" for our service!
 ┗ 📜 README.md
```

---

## ⚡ Prerequisites

To run this on your computer, you'll need:

-   **Java JDK 8+** (for the Service).
    -   *Note: If using JDK 11+, ensure JAX-WS dependencies are available.*
-   **Python 3.13+** (for the Client).

---

## 🔧 Generation Logic

The Java source code for the service interface was generated using the `wsimport` tool, which parses the WSDL file and creates the necessary Java classes.

**Command used:**
```bash
wsimport -keep -s . calculator.wsdl
```
*This command created the interface and helper classes (like `CalculatorPortType`). We then manually wrote `Calculator.java` to implement the actual logic.*

---

## 🏃‍♂️ How to Run It

### 1. Start the Server (Java)

Go into the `Service` folder and run these commands to start the calculator server.

```bash
cd Service
# 1. Compile the code
javac Main.java com/calc/*.java

# 2. Start the server
java Main
```

You should see:
```
The server is running...
http://localhost:8080/calc?wsdl
```
*The service is now active and listening for requests.*

### 2. Run the Client (Python)

Open a new terminal, navigate to the `Client` directory, and install dependencies.

```bash
cd Client
# Install zeep (if not already installed)
pip install zeep

# Run the client
python main.py
```

**Expected Output:**
```
45
```
*(Calculated result of 15 + 30)*

---

## 📚 Resources 


**Key Tools:**
*   [wsimport](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/wsimport.html): Utilized for generating portable artifacts from WSDL.
*   [Zeep](https://docs.python-zeep.org/): A modern, fast Python SOAP client.

**References:**
*   📺 **Python Client**: [Identify & Implement SOAP Services](https://www.youtube.com/watch?v=JBYEQjg_znI) - The core tutorial guiding this implementation.

---
## 🧪 Testing with Postman
*   [SOAP Request in Postman](https://www.youtube.com/watch?v=V0yEzwFe5pw)

```xml
<?xml version="1.0" encoding="utf-8"?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
    <S:Body>
        <ns2:Add xmlns:ns2="http://calc.com/">
            <num1>20</num1>
            <num2>30</num2>
        </ns2:Add>
    </S:Body>
</S:Envelope>
```