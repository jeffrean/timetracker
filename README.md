# timetracker
Open source replica of Timeular's time tracking functionality

# Basic First Time Behavior
1. user registers
2. user searches for nearby devices
3. user pairs to device with bluetooth
4. user gives wifi credentials to device
5. device starts caching data and posting as frequently as possible

# Server Structure
* API - /api/
	* /users/<string:user>/device-id/ (PUT)
		* params: device id
	* /users/<string:user>/timestamps/ (POST)
		* provide device id along with auth? 
		* params: tracker side, timestamp
	* /users/<string:user>/timestamps?begin=<datetime:begin>&end=<datetime:end>/
		* maybe put begin and end in body?
