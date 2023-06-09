import argparse
from app.ams_data_processor import main
import pyinstrument
from pyinstrument import Profiler

if __name__ == '__main__':


    # Create a profiler instance
    profiler = Profiler()

    # Start profiling
    profiler.start()
    # print(profiler.output_text(unicode=True, color=True))

    parser = argparse.ArgumentParser(description='AMS file processing')
    parser.add_argument('file_path', type=str, help='Path to the AMS measurement file')
    parser.add_argument('formula', type=str, help='Mathematical formula to be applied')
    parser.add_argument('output_dir', type=str, help='Directory to store the output files')
    args = parser.parse_args()

    main(args.file_path, args.formula, args.output_dir)
    # Stop profiling
    profiler.stop()

# Print the profiling results
    print(profiler.output_text(unicode=True, color=True))
    # Generate an HTML call graph
    html_output = profiler.output_html()

    # Save the HTML output to a file
    with open('call_graph.html', 'w') as f:
        f.write(html_output)
