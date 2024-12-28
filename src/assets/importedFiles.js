let {
    VITE_FOLDER_PY
} = import.meta.env

const importedfiles = [
    "/py/main.py"
]

export default importedfiles.map(e => VITE_FOLDER_PY + e)