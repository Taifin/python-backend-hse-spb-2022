# gRPC calculator

A simple server that can calculate basic expressions of two arguments with next operations: `+`, `-`, `//`, `%`, `*`, `**`.

## Compiling and running

1. Compile protobuf files with

    ```sh
    python -m grpc_tools.protoc -Iapp/proto --python_out=. --grpc_python_out=. app/proto/services.proto    
    ```

2. Run server with `python ./app/server.py`.

3. Run client with `python ./app/client.py`. The application will wait until you enter two numbers in a row, a newline and an operation.

4. Do not forget to shut the server down!

## Testing

To run tests, execute `python ./app/tests/EvalTest.py`. Remember to run the server first!
