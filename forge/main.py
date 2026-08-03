from forge.plugins.manager import PluginManager


def main():

    print()

    print("========== ForgeAI ==========")

    print()

    manager = PluginManager()

    manager.discover()

    manager.initialize()

    print()

    print("Loaded Plugins")

    for plugin in manager.plugins:

        print("-", plugin.name)

    print()

    print("Capabilities")

    for cap in manager.capabilities():

        print("-", cap.name)


if __name__ == "__main__":

    main()