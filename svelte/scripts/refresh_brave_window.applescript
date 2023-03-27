-- finds Brave Browser, focusses on tab with specified title and reloads
tell application "Brave Browser"
    repeat with w in (windows)
        set j to 0
        repeat with t in (tabs of w)
            set j to j + 1
            if title of t contains "lorecraft-client-new" then
                set (active tab index of w) to j
                reload active tab of w
                return
            end if
        end repeat
    end repeat
end tell
