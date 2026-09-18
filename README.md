\# 🔬 4-Bit Stuck-at Fault Simulator



\## 📌 Project Overview



The \*\*4-Bit Stuck-at Fault Simulator\*\* is a digital logic fault simulation application developed for a DELD project.



The application simulates a \*\*4-bit Ripple Carry Adder\*\* and identifies input test vectors that can detect stuck-at faults at different circuit wires.



The simulator supports:



\* Stuck-at-0 faults

\* Stuck-at-1 faults

\* Sum-wire faults

\* Carry-wire faults

\* Exhaustive testing of all 256 input combinations

\* Fault detection coverage calculation

\* Display of normal and faulty outputs

\* Download of detected test vectors as a CSV file



\---



\## 🎯 Objectives



1\. Understand the concept of stuck-at faults.

2\. Implement a gate-level 4-bit Ripple Carry Adder.

3\. Inject faults into internal circuit wires.

4\. Compare fault-free and faulty circuit outputs.

5\. Identify test vectors that detect the injected fault.

6\. Calculate fault detection coverage.

7\. Develop a web-based interface using Streamlit.



\---



\## 🧠 Fault Model



The project uses the \*\*single stuck-at fault model\*\*.



A circuit wire can be assumed to be permanently fixed at either:



```text

Stuck-at-0

```



or



```text

Stuck-at-1

```



For example:



```text

S2 stuck-at-0

```



means that the S2 wire is forced to logic 0 regardless of its normal circuit value.



\---



\## ⚙️ Circuit



The simulator uses a 4-bit Ripple Carry Adder.



The circuit has:



\### Inputs



```text

A\[3:0]

B\[3:0]

```



\### Outputs



```text

S\[3:0]

Cout

```



\### Fault locations



```text

S0

S1

S2

S3



C1

C2

C3

C4

```



\---



\## 🔬 Working Principle



The simulator performs the following steps:



```text

Start

&#x20;  ↓

Select Fault Wire

&#x20;  ↓

Select Stuck-at Value

&#x20;  ↓

Generate All 256 Input Vectors

&#x20;  ↓

Simulate Fault-Free Circuit

&#x20;  ↓

Inject Fault

&#x20;  ↓

Simulate Faulty Circuit

&#x20;  ↓

Compare Outputs

&#x20;  ↓

If Outputs Differ

&#x20;  ↓

Fault Detected

&#x20;  ↓

Display Test Vectors

```



\---



\## 🧮 Full Adder Equations



The Sum output is:



```text

S = A XOR B XOR Cin

```



The Carry output is:



```text

Cout = AB + BCin + ACin

```



Four full adders are connected to create the 4-bit Ripple Carry Adder.



\---



\## 📊 Fault Detection



For every combination of A and B:



```text

16 × 16 = 256

```



input vectors are tested.



The fault-free output is compared with the faulty output.



If:



```text

Normal Output ≠ Faulty Output

```



then the input vector detects the fault.



\---



\## 📈 Fault Detection Coverage



The application calculates:



```text

Fault Coverage (%) =

(Number of Detecting Test Vectors /

&#x20;Total Test Vectors) × 100

```



Since there are 256 possible A/B combinations:



```text

Total Test Vectors = 256

```



\---



\## 💻 Technologies Used



\* Python

\* Streamlit

\* Pandas

\* Digital Logic

\* Fault Simulation

\* Git

\* GitHub



\---



\## 📁 Project Structure



```text

4-Bit-Stuck-At-Fault-Simulator

│

├── app.py

├── requirements.txt

├── README.md

└── .gitignore

```



\---



\## 🚀 Running the Application Locally



\### Step 1: Install Python



Check Python:



```cmd

py --version

```



\### Step 2: Install dependencies



```cmd

py -m pip install -r requirements.txt

```



\### Step 3: Run Streamlit



```cmd

py -m streamlit run app.py

```



The terminal will display a local address similar to:



```text

http://localhost:8501

```



Open that address in a web browser.



\---



\## 🧪 Example



Select:



```text

Fault Wire: S2

Fault Type: Stuck-at-0

```



Click:



```text

RUN FAULT SIMULATION

```



The application tests all 256 possible input combinations and displays the test vectors for which the normal and faulty outputs differ.



\---



\## 📥 Output



The application displays:



\* Total test vectors

\* Number of detected vectors

\* Fault detection coverage

\* Input A

\* Input B

\* Normal output

\* Faulty output



The detected vectors can also be downloaded as:



```text

detected\_test\_vectors.csv

```



\---



\## 🌐 Deployment



The application can be deployed using \*\*Streamlit Community Cloud\*\*.



The GitHub repository should contain:



```text

app.py

requirements.txt

README.md

.gitignore

```



The main application file is:



```text

app.py

```



\---



\## 👩‍💻 Project



\*\*Project:\*\* 4-Bit Stuck-at Fault Simulator



\*\*Domain:\*\* Digital Electronics and Digital Logic Design



\*\*Platform:\*\* Streamlit



\*\*Language:\*\* Python



\*\*Purpose:\*\* Educational fault simulation and test-vector generation



