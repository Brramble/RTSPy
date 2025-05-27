# RTSPy

A lightweight RTSP stream relay server built with Python and Flask. This application allows you to view RTSP camera streams in a web browser by converting them to MJPEG format.

## Features

- Convert RTSP streams to MJPEG for browser compatibility
- Simple YAML-based configuration
- Docker support
- Full-screen video display
- Multiple stream support
- Low latency streaming

## Prerequisites

- Python 3.11 or higher
- FFmpeg
- Docker (optional)

## Installation

### Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RTSPy.git
   cd RTSPy
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Docker Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RTSPy.git
   cd RTSPy
   ```

2. Build and run with Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Configuration

1. Copy the example configuration file:
   ```bash
   cp streams.yaml.example streams.yaml
   ```

2. Edit `streams.yaml` with your RTSP stream URLs:
   ```yaml
   front_door:
     rtsp://username:password@camera-ip:554/stream1
   ```

## Usage

### Local Usage

1. Start the server:
   ```bash
   python app.py
   ```

2. Access streams in your browser:
   - Front door: `http://localhost:8700/front_door`
   - Backyard: `http://localhost:8700/backyard`
   - Garage: `http://localhost:8700/garage`

### Docker Usage

The server will be available at `http://localhost:8700` after starting with Docker Compose.

## Environment Variables

- `STREAMS_CONFIG`: Path to the streams configuration file (default: `streams.yaml`)

## Security Considerations

- The `streams.yaml` file contains sensitive information and should not be committed to version control
- Consider using environment variables for stream credentials in production
- The application runs on port 8700 by default - ensure this port is properly secured

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
