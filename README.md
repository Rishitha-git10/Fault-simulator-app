# Fault-simulator-app
A Streamlit-based 4-Bit Stuck-at Fault Simulator that injects stuck-at-0 and stuck-at-1 faults into a 4-bit Ripple Carry Adder and identifies test vectors that detect the faults.
# 🔬 4-Bit Stuck-at Fault Simulator

## 📌 Project Overview

The **4-Bit Stuck-at Fault Simulator** is a digital logic fault simulation application developed using **Python and Streamlit** as a DELD (Digital Electronics and Logic Design) project.

The application simulates a **4-bit Ripple Carry Adder** and injects different stuck-at faults into its internal wires. It then checks all possible input combinations and identifies the test vectors that can detect the selected fault.

The simulator supports:

- Stuck-at-0 faults
- Stuck-at-1 faults
- Sum wire faults
- Carry wire faults
- Automatic generation of test vectors
- Fault detection comparison
- Fault detection coverage calculation
- CSV download of detected test vectors

---

## 🎯 Objectives

The main objectives of this project are:

1. To understand the concept of fault simulation in digital circuits.
2. To implement a 4-bit Ripple Carry Adder using Python.
3. To simulate stuck-at-0 and stuck-at-1 faults.
4. To generate input test vectors automatically.
5. To compare normal and faulty circuit outputs.
6. To identify test vectors that detect a fault.
7. To calculate fault detection coverage.
8. To provide a simple web interface using Streamlit.

---

## ⚡ Circuit Used

The simulator uses a **4-bit Ripple Carry Adder**.

### Inputs

```text
A[3:0]
B[3:0]
