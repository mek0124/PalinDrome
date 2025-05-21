<label id="top"></label>

<div align="center">
  <img src="./app-icon.jpeg" height="120" width="120" />
  <h1>PalinDrome</h1>
</div>

A simple desktop application for checking if your word or phrase is the same spelled forwards as it is backwards.

## How To Use

1. Clone the Repo

    ```
    git clone https://github.com/mek0124/PalinDrome.git
    ```

2. To run the app

    ```
    bash run.sh
    ```

    - This script is setup to convert all .ui files found in src/ to .py files before packaging.

    - This script is setup to automatically check for the `dist` and `build` folders for the project. If they do not exist, it will build the application down and launch it for you.

## Updating

This application comes with a method to check the current version (in the app/version.txt) versus the latest release on GitHub. If these versions <b><u>do not match</u></b> the application will <b><u>prompt for an update</u></b>. If you <b><u>do not want to update</u></b> then click **No** on the popup dialog. Keep in mind, you will be <b><u>prompted to update</u></b> on each launch. This is because (but not limited to) any updates that may come along, changes in client-side frameworks, api's libraries, etc.

## Features

- Checks if a word, or phrase, is the same forwards and backwards
- Option to ignore CaseSensitivity with spelling
- Ignores all punctuation.
- Update feature to assist in maintaining the code base

## Issues

If at any point you come into any issues, please create [a new issue](https://github.com/mek0124/PalinDrome/issues) and I will respond as soon as I can. If you do not get a response from me, be sure to check the repo for updates. 