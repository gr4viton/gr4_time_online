schtasks /query /tn gr4_time_online_onlogon 
IF %ERRORLEVEL% EQU 1 (
    ECHO aa
    schtasks /create /tn gr4_time_online_onlogon /tr gr4_time_online_update.bat /sc onlogon
    ECHO Task gr4_time_online_onlogon scheduled succesfully
) ELSE (
    ECHO Task gr4_time_online_onlogon already scheduled, proceeding to delete the task.
    schtasks /delete /tn gr4_time_online_onlogon    
)


