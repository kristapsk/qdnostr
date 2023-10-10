import time
import toml
from nostr.event import Event, EventKind
from nostr.key import PrivateKey
from nostr.relay_manager import RelayManager


relay_manager = RelayManager()


def connect_to_relays(relay_list_file: str = 'relays.txt'):

    with open(relay_list_file) as f:
        relays = f.readlines()

    for relay in relays:
        relay = relay.strip()
        print('add_relay: ' + relay)
        relay_manager.add_relay(url=relay)

    time.sleep(2)


def publish_note(nsec: str, content: str):
    event = Event(content=content, kind=EventKind.TEXT_NOTE)
    privkey = PrivateKey.from_nsec(nsec)
    privkey.sign_event(event)
    print('calling publish_event: ' + content)
    print(event.note_id)
    relay_manager.publish_event(event)
    time.sleep(1)


def disconnect_from_relays():
    relay_manager.close_all_relay_connections()

