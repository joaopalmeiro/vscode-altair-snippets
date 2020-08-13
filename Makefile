SRC_DIR := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
SRC_DIR_NAME := $(notdir $(realpath $(SRC_DIR)))

VSCODE_DIR := ~/.vscode/extensions
DEST_DIR := $(VSCODE_DIR)/$(SRC_DIR_NAME)/

.PHONY: copy clean

copy:
	@echo "Copying files..."

	rm -rf $(DEST_DIR)
	cp -R $(SRC_DIR) $(DEST_DIR)

	@echo "Done!"

clean:
	@echo "Removing files..."

	rm -rf $(DEST_DIR)

	@echo "Done!"
