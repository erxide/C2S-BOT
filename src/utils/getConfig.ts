import type { Config } from '../types';

export const getConfig = async (configPath:URL):Promise<Config> => {
    return await Bun.file(configPath).json();
};