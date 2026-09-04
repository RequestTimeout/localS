try:
    import argparse
    import os
    import subprocess

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-p", action="store")
    parser.add_argument("-d", action="store")
    parser.add_argument("--help", action="store_true")

    args, unknown = parser.parse_known_args()

    if unknown:
        print("Error: Unknown arguments: {}\nUse '--help' for more information".format(unknown))
        exit()
    if args.help:
        print("""Usage: server -p <port> -d <directory>
Start a local HTTP server for the specified directory.""")
        exit()
    if os.path.exists(args.d):
        if args.p:
            if 1 <= int(args.p) <= 65535:
                subprocess.run(
                    "start 'server - port: %PORT%' /min /wait python -m http.server {} -d {} >nul 2>&1"
                    .format(int(args.p), args.d), shell=True)
                print("Server started on port {} at http://localhost:{}.".format(int(args.p), int(args.p)))
            else:
                print("Error: Invalid port number: {}\nUse '--help' for more information".format(args.p))
        else:
            print("Error: Please enter a port number\nUse '--help' for more information")
    else:
        print("Error: {} does not exist\nUse '--help' for more information".format(args.d))
except ValueError as e:
    ...
