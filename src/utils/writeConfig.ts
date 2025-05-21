import type { Config } from '../types';

export const writeConfig = async (configPath:URL, newConfig:Config):Promise<Config> => {
    await Bun.write(configPath, JSON.stringify(newConfig, null, 2));
    return newConfig;
};