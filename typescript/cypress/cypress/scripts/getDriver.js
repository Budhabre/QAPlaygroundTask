const configJson = require("../fixtures/config.json");

const driverName = process.env.CFG_DRIVER_NAME ?? configJson.driver_name;
const normalizedDriverName = driverName.toLowerCase();

process.stdout.write(normalizedDriverName);
