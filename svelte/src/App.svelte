<script>
  import { afterUpdate } from "svelte";
  import { Button, Popover } from "sveltestrap";

  let name;
  let desc;
  let contents = [];
  let characters = [];
  let exits = [];
  let msgToEvennia;
  let echoLogs = [];
  let scrollableDiv;

  const placements = ['top', 'right', 'left', 'bottom'];

  afterUpdate(() => {
    scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);
  });

  function handleWindowLoad() {
    Evennia.init();
    window.Evennia.emitter.on("room_data", function (empty, roomData) {
      name = roomData.name;
      desc = roomData.desc;
      contents = _formatContents(roomData.contents);
      characters = _formatCharacters(roomData.characters);
      exits = roomData.exits.filter((exit) => {
        return (
          exit === "north" ||
          exit === "south" ||
          exit === "east" ||
          exit === "west"
        );
      });
    });
    window.Evennia.emitter.on("text", function (text, cmd) {
      if (cmd.type === "look") {
        return;
      }
      echoLogs = [...echoLogs, text[0]];
    });
  }

  function handleClickExit(exit) {
    Evennia.msg("text", [exit]);
    echoLogs = [];
  }

  function handleClickTitle() {
    Evennia.msg("text", ["look"]);
    echoLogs = [];
  }

  function onSubmit(e) {
    Evennia.msg("text", [msgToEvennia]);
    msgToEvennia = "";
  }

  function _formatContents(contents) {
    let roomItems = contents.map((item) => `a ${item}`);

    if (roomItems.length === 1) {
      return `You see ${roomItems[0]}.`;
    }
    if (roomItems.length > 1) {
      let lastItem = roomItems.pop();
      return `You see ${roomItems.join(", ")}, and ${lastItem}.`;
    }
    return null;
  }

  function _formatCharacters(characters) {
    let str;

    if (characters.length === 1) {
      return _upcaseFirstChar(`${characters[0]} is here.`);
    }
    if (characters.length === 2) {
      return _upcaseFirstChar(
        `${characters[0]} and ${characters[1]} are here.`
      );
    }
    if (characters.length > 2) {
      let lastChar = characters.pop();
      return _upcaseFirstChar(
        `${characters.join(", ")}, and ${lastChar} are here.`
      );
    }
  }

  function _upcaseFirstChar(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }
</script>

<svelte:window on:load={handleWindowLoad} />

<main>
  <section class="room-info">
    <h1 on:click={handleClickTitle}>{name}</h1>
    <p>{@html desc}</p>
    {#if contents}
      <p>
        {contents}
        {#if characters}
          <span>{characters}</span>
        {/if}
      </p>
    {/if}

    <p>
      {#if exits.length > 0}
        You can go
      {/if}
      {#each exits as exit}
        <button on:click={() => handleClickExit(exit)}>{exit}</button><span
          >&nbsp;</span
        >
      {/each}
    </p>
  </section>

  <div class="mt-3">
	<Button id='btn-bottom'>Click for bottom</Button>
	<Popover
	  target='btn-bottom'
	  placement='bottom'
	>
	  This is a Popover on the Bottom of the trigger.
	</Popover>
  </div>

  <section bind:this={scrollableDiv} class="echo-log">
    {#each echoLogs as exit}
      <p>{@html exit}</p>
    {/each}
  </section>

  <form class="msg-to-evennia" on:submit|preventDefault={onSubmit}>
    <input bind:value={msgToEvennia} type="text" />
  </form>
</main>

<style>
  main {
    text-align: center;
    padding: 2em;
    margin: 0 auto;
    line-height: 1.5rem;
    display: flex;
    flex-direction: column;
    height: 89vh;
    overflow: hidden;
  }

  .room-info {
    flex: 0 0 auto;
  }

  .echo-log {
    flex: 1 1 auto;
    overflow-y: scroll;
    margin-right: -60px;
    padding-right: 40px;
    scroll-behavior: smooth;
  }

  .msg-to-evennia {
    flex: 0 0 auto;
  }

  input {
    width: 100%;
  }

  p {
    text-align: left;
    word-wrap: break-word;
  }

  p::first-letter {
    text-transform: capitalize;
  }

  h1 {
    text-transform: uppercase;
    font-size: 3em;
    font-weight: 100;
    margin-bottom: 2rem;
  }

  button {
    text-decoration: underline;
    background-color: transparent;
    border-width: 0;
    font-family: inherit;
    font-size: inherit;
    font-style: inherit;
    font-weight: inherit;
    line-height: inherit;
    padding: 0;
  }
  button:hover {
    cursor: pointer;
    color: rgb(255, 183, 183);
    text-decoration: underline;
  }
</style>
