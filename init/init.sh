
. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT
trap 'echo hi' USR1

initPetercord() {
    printLogo
    assertPrerequisites
    sendMessage "Initializing Petercord ..."
    assertEnvironment
    editLastMessage "Starting Petercord ..."
    printLine
}

startPetercord() {
    startLogBotPolling
    runPythonModule petercord "$@"
}

stopPetercord() {
    sendMessage "Exiting Petercord ..."
    endLogBotPolling
}

handleSigTerm() {
    log "Exiting With SIGTERM (143) ..."
    stopPetercord
    exit 143
}

handleSigInt() {
    log "Exiting With SIGINT (130) ..."
    stopPetercord
    exit 130
}

runPetercord() {
    initPetercord
    startPetercord "$@"
    local code=$?
    stopPetercord
    return $code
}
