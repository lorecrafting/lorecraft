const watch = require('node-watch');
const { exec } = require("child_process");

watch('./src', { recursive: true }, function(evt, name) {
    console.log('%s changed.', name);
    exec("npm run build && evennia collectstatic --noinput && osascript ./scripts/refresh_brave_window.applescript", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });
  });
