{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/packages/
  packages = [
    pkgs.git
  ];

  # https://devenv.sh/services/
  services.postgres = {
    enable = true;
    package = pkgs.postgresql_15;
    initialDatabases = [{ name = "dinedine"; }];
    listen_addresses = "127.0.0.1";
    port = 5432;
    extensions = extensions: [ extensions.postgis extensions.pgvector ];
    initialScript = ''
      CREATE USER dinedine;
      ALTER DATABASE dinedine OWNER TO dinedine;
      GRANT ALL PRIVILEGES ON DATABASE dinedine TO dinedine;
      ALTER USER dinedine WITH SUPERUSER;
    '';
  };

  dotenv.enable = true;

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    venv = {
      enable = true;
      requirements = builtins.readFile ./requirements.txt;
    };
  };

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
