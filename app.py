from flask import Flask, render_template, request

app = Flask(__name__)


def full_adder(a, b, cin):
    s = a ^ b ^ cin
    cout = (a & b) | (cin & (a ^ b))
    return s, cout


def ripple_carry_adder(A, B, cin=0):

    S = [0, 0, 0, 0]
    C = [0, 0, 0, 0, 0]

    C[0] = cin

    for i in range(4):
        S[i], C[i + 1] = full_adder(
            A[i],
            B[i],
            C[i]
        )

    return S, C[4]


def simulate_fault(A, B, fault_wire, stuck_value):

    normal_S, normal_Cout = ripple_carry_adder(A, B)

    faulty_S = normal_S.copy()
    faulty_Cout = normal_Cout

    if fault_wire == "S0":
        faulty_S[0] = stuck_value

    elif fault_wire == "S1":
        faulty_S[1] = stuck_value

    elif fault_wire == "S2":
        faulty_S[2] = stuck_value

    elif fault_wire == "S3":
        faulty_S[3] = stuck_value

    elif fault_wire == "C1":

        carry = stuck_value

        for i in range(1, 4):
            faulty_S[i], carry = full_adder(
                A[i],
                B[i],
                carry
            )

        faulty_Cout = carry

    elif fault_wire == "C2":

        carry = stuck_value

        for i in range(2, 4):
            faulty_S[i], carry = full_adder(
                A[i],
                B[i],
                carry
            )

        faulty_Cout = carry

    elif fault_wire == "C3":

        faulty_S[3], faulty_Cout = full_adder(
            A[3],
            B[3],
            stuck_value
        )

    elif fault_wire == "C4":

        faulty_Cout = stuck_value

    return faulty_S, faulty_Cout


def make_bits(number):

    return [
        (number >> 0) & 1,
        (number >> 1) & 1,
        (number >> 2) & 1,
        (number >> 3) & 1
    ]


def bits_to_string(bits):

    return "".join(
        str(bit) for bit in reversed(bits)
    )


def generate_test_vectors(fault_wire, stuck_value):

    detected = []

    for A_value in range(16):

        for B_value in range(16):

            A = make_bits(A_value)
            B = make_bits(B_value)

            normal_S, normal_Cout = ripple_carry_adder(
                A,
                B
            )

            faulty_S, faulty_Cout = simulate_fault(
                A,
                B,
                fault_wire,
                stuck_value
            )

            normal_output = (
                str(normal_Cout) +
                bits_to_string(normal_S)
            )

            faulty_output = (
                str(faulty_Cout) +
                bits_to_string(faulty_S)
            )

            if normal_output != faulty_output:

                detected.append({
                    "A": bits_to_string(A),
                    "B": bits_to_string(B),
                    "normal": normal_output,
                    "faulty": faulty_output
                })

    return detected


@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    fault_wire = ""
    stuck_value = ""
    total = 0

    if request.method == "POST":

        fault_wire = request.form["fault_wire"]
        stuck_value = request.form["stuck_value"]

        results = generate_test_vectors(
            fault_wire,
            int(stuck_value)
        )

        total = len(results)

    return render_template(
        "index.html",
        results=results,
        fault_wire=fault_wire,
        stuck_value=stuck_value,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)