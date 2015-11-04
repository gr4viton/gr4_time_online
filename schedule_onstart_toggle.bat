schtasks /query /tn gr4_time_online_onstart 
IF %ERRORLEVEL% EQU 1 (
    ECHO aa
    schtasks /create /tn gr4_time_online_onstart /tr gr4_time_online_update.bat /sc onstart /V1
    ECHO Task gr4_time_online_onstart scheduled succesfully
) ELSE (
    ECHO Task gr4_time_online_onstart already scheduled, proceeding to delete the task.
    schtasks /delete /tn gr4_time_online_onstart    
)


