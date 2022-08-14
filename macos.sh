#!/usr/bin/env bash
sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value = $imagePath";
killall Dock;