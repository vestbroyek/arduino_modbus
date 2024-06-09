import time
from pymodbus.client import ModbusTcpClient
from pymodbus import Framer


LOOP_COUNT = 50
REGISTER_COUNT = 10
INPUT_REGISTER = 100
HOST_IP = "192.168.0.177"


def run_sync_client_test():
    client = ModbusTcpClient(
        host=HOST_IP,
        framer=Framer.SOCKET,
        baudrate=9600
    )
    client.connect()
    assert client.connected, "Could not connect to server"

    start_time = time.time()
    for _i in range(LOOP_COUNT):
        rr = client.read_input_registers(INPUT_REGISTER, REGISTER_COUNT, slave=1)
        if rr.isError():
            print(f"Received Modbus library error({rr})")
            break
        else:
            print(f"Read value {rr.registers[0]}")
    client.close()
    run_time = time.time() - start_time
    avg_call = (run_time / LOOP_COUNT) * 1000
    avg_register = avg_call / REGISTER_COUNT
    print(
        f"running {LOOP_COUNT} call (each {REGISTER_COUNT} registers), took {run_time:.2f} seconds"
    )
    print(f"Averages {avg_call:.2f} ms pr call and {avg_register:.2f} ms pr register.")

if __name__ == "__main__":
    run_sync_client_test()