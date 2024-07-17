import { exec } from 'child_process';

const viteProcess = exec('npm run dev');

viteProcess.stdout.on('data', (data) => {
  console.log(data.toString());
});

viteProcess.stderr.on('data', (data) => {
  console.error(data.toString());
});

process.on('exit', () => {
  viteProcess.kill();
});

process.on('SIGINT', () => {
  process.exit();
});

process.on('SIGTERM', () => {
  process.exit();
});
