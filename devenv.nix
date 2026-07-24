{ pkgs, lib, config, inputs, ... }:

{
  packages = [ pkgs.git ];

  languages.python = {
    enable = true;
    version = "3.14";
    venv = {
      enable = true;
      requirements = ./requirements.txt;
    };
  };
}
