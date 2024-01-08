import { defineConfig } from "cypress";
import * as fs from "fs";
import * as path from "path";
import { config } from "dotenv";
import { normalizeEnv } from "./cypress/support/utils";

const env = config().parsed;

const configJson = JSON.parse(
  fs.readFileSync(
    path.join(__dirname, "./cypress/fixtures/config.json"),
    "utf8"
  )
);

const mergedEnv = {
  ...normalizeEnv(configJson),
  ...normalizeEnv(env),
  ...normalizeEnv(process.env),
};

export default defineConfig({
  env: mergedEnv,

  e2e: {
    setupNodeEvents(on, config) {
      config.baseUrl = mergedEnv.BASE_URL ?? "";
      return config;
    },
  },
});
