import os

def main():
    if not os.path.isdir("result"):
        os.makedirs("result")

    for i in range(27):
        filename = f"image-000{i:02d}.dcm"
        input_path = os.path.join(os.getcwd(), "series-00003", filename)
        output_path = os.path.join(os.getcwd(), "result", filename)

        if os.system(f"gdcmconv --raw {input_path} {output_path}") == 0:
            print("Success.")
        else:
            print("Failure.")

if __name__ == "__main__":
    main()