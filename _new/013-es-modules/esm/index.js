import fs from 'fs';
import crypto from 'crypto';

import util from './util.js';

let contents = await util.open('package.json');

console.log(contents);
