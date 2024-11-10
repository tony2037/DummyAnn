#!/bin/bash

# Function to detect the operating system
detect_os() {
    case "$(uname -s)" in
        Darwin*)    echo "macOS" ;;
        CYGWIN*|MINGW32*|MSYS*|MINGW*) echo "Windows" ;;
        *)          echo "Unsupported OS" ;;
    esac
}

# Function to install Ollama on macOS
install_ollama_macos() {
    echo "Installing Ollama on macOS..."
    if command -v brew &>/dev/null; then
        brew install ollama
    else
        echo "Homebrew is not installed. Installing Homebrew first..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        brew install ollama
    fi
}

# Function to install Ollama on Windows
install_ollama_windows() {
    echo "Installing Ollama on Windows..."
    if command -v winget &>/dev/null; then
        winget install Ollama.Ollama
    else
        echo "WinGet is not available. Please install Ollama manually from https://ollama.com/"
        exit 1
    fi
}

# Main installation logic
main() {
    OS=$(detect_os)
    case $OS in
        "macOS")
            install_ollama_macos
            ;;
        "Windows")
            install_ollama_windows
            ;;
        *)
            echo "Unsupported operating system. Please install Ollama manually from https://ollama.com/"
            exit 1
            ;;
    esac

    echo "Ollama installation completed. Please restart your terminal or command prompt."
}

# Run the main function
main
