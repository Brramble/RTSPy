# RTSPy

A lightweight RTSP stream relay server built with Python and Flask. This application allows you to view RTSP camera streams in a web browser by converting them to MJPEG format.

## Features

- Convert RTSP streams to MJPEG for browser compatibility
- Environment variable based configuration
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

### Environment Variables

The application uses environment variables to configure RTSP streams. Each stream should be configured using the format:

```
STREAM_<NAME>=rtsp://username:password@camera-ip:port/stream-path
```

For example:
```bash
STREAM_FRONT_DOOR=rtsp://admin:password@192.168.1.100:554/stream1
STREAM_BACKYARD=rtsp://admin:password@192.168.1.101:554/stream1
```

### Docker Compose Configuration

You can configure streams in your `docker-compose.yml`:

```yaml
services:
  rtsp-relay:
    environment:
      - STREAM_FRONT_DOOR=rtsp://admin:password@192.168.1.100:554/stream1
      - STREAM_BACKYARD=rtsp://admin:password@192.168.1.101:554/stream1
```

## Usage

### Local Usage

1. Set environment variables for your streams:
   ```bash
   export STREAM_FRONT_DOOR=rtsp://admin:password@192.168.1.100:554/stream1
   ```

2. Start the server:
   ```bash
   python app.py
   ```

3. Access streams in your browser:
   - Front door: `http://localhost:8700/front_door`
   - Backyard: `http://localhost:8700/backyard`
   - Garage: `http://localhost:8700/garage`

### Docker Usage

The server will be available at `http://localhost:8700` after starting with Docker Compose.

## Security Considerations

- Store sensitive credentials in environment variables or Docker secrets
- The application runs on port 8700 by default - ensure this port is properly secured
- Consider using Docker secrets for production deployments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
