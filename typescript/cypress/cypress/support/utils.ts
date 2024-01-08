export const normalizeEnvKey = (key: string) => {
  const normalizedKey = key.toUpperCase();
  if (normalizedKey.startsWith("CFG_")) {
    return normalizedKey.substring(4);
  }
  return normalizedKey;
};

export const normalizeEnv = (env?: Record<string, string | undefined>) => {
  if (!env) return {};
  const normalizedEnv: Record<string, string | undefined> = {};
  Object.keys(env).forEach((key) => {
    normalizedEnv[normalizeEnvKey(key)] = env[key];
  });
  return normalizedEnv;
};

export const env = (key: string) => {
  return Cypress.env(normalizeEnvKey(key));
};
