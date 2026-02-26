### Project folder must include a .env and .onboard.env

.env includes the following values:
* DRONE_TOKEN (uuid for authorization to communicate with the backend)
* BACKEND_URL

.onboard.env includes the following values:
* DRONE_PI_IP (IP of onboard Pi, static for testing)
* DRONE_PI_USER (onboard Pi user)
* LOCAL_FILE=/home/sr-design/agrodrone-system/flightplans/waypoints.json (location on edge node)
* REMOTE_DEST (where the onboard Pi will read the waypoints)
