import tortilla_pb2
from google.protobuf import text_format

program = tortilla_pb2.ProgramGraph()
with open("sam.pbtxt", "rb") as f:
        fd = f.read()
        text_format.Parse(fd, program)
        # print(tortilla)
program_name = program.name
operators = program.operators

for operator in operators:
        operator_name = operator.name
        operator_id = operator.id
        operator_op = operator.WhichOneof("op")

        if operator_op == "broadcast":
            broadcast_op = operator.broadcast
            # print(broadcast_op.output)
            input_id = broadcast_op.input.id
            output_id = broadcast_op.output[0].id

        #     printing broadcast operators
            print(f"Operator: {operator_name}")
            print(f"ID: {operator_id}")
            print(f"Input ID: {input_id}")
            print(f"Output ID: {output_id}")
        elif operator_op == "fiber_lookup":
            fiber_op = operator.fiber_lookup
            # print(broadcast_op.output)
        #     input_id = fiber_op.input.id
            output_id = fiber_op.output_ref.id
            crd_output_id = fiber_op.output_crd.id

        #     printing broadcast operators
            print(f"Operator: {operator_name}")
            print(f"ID: {operator_id}")
            print(f"Output ID: {output_id}")
        # print(operator)
