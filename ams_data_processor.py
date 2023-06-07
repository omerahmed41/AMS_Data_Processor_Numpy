from app.ams_data_processor import main

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='AMS file processing')
    parser.add_argument('file_path', type=str, help='Path to the AMS measurement file')
    parser.add_argument('formula', type=str, help='Mathematical formula to be applied')
    parser.add_argument('output_dir', type=str, help='Directory to store the output files')
    args = parser.parse_args()

    main(args.file_path, args.formula, args.output_dir)
