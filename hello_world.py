from asyncflows import AsyncFlows

import asynflows 
async def main():
    # Load the flow from the file
    flow = AsyncFlows.from_file("hello_world.yaml")

    # Run the flow
    result = await flow.set_vars(name="SHIRLYN CLARE").run()

    # Print the result
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
