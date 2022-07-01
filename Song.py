from enum import Enum
from typing import List, Union
from datetime import datetime


class Cursors:
    after: str
    before: str

    def __init__(self, after: str, before: str) -> None:
        self.after = after
        self.before = before


class AlbumTypeEnum(Enum):
    ALBUM = "album"
    COMPILATION = "compilation"
    SINGLE = "single"


class ExternalUrls:
    spotify: str

    def __init__(self, spotify: str) -> None:
        self.spotify = spotify


class ArtistType(Enum):
    ARTIST = "artist"


class Artist:
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: ArtistType
    uri: str

    def __init__(self, external_urls: ExternalUrls, href: str, id: str, name: str, type: ArtistType, uri: str) -> None:
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.name = name
        self.type = type
        self.uri = uri


class Image:
    height: int
    url: str
    width: int

    def __init__(self, height: int, url: str, width: int) -> None:
        self.height = height
        self.url = url
        self.width = width


class ReleaseDatePrecision(Enum):
    DAY = "day"
    YEAR = "year"


class Album:
    album_type: AlbumTypeEnum
    artists: List[Artist]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: Union[datetime, int]
    release_date_precision: ReleaseDatePrecision
    total_tracks: int
    type: AlbumTypeEnum
    uri: str

    def __init__(self, album_type: AlbumTypeEnum, artists: List[Artist], available_markets: List[str], external_urls: ExternalUrls, href: str, id: str, images: List[Image], name: str, release_date: Union[datetime, int], release_date_precision: ReleaseDatePrecision, total_tracks: int, type: AlbumTypeEnum, uri: str) -> None:
        self.album_type = album_type
        self.artists = artists
        self.available_markets = available_markets
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.images = images
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.total_tracks = total_tracks
        self.type = type
        self.uri = uri


class ExternalIDS:
    isrc: str

    def __init__(self, isrc: str) -> None:
        self.isrc = isrc


class TrackType(Enum):
    TRACK = "track"


class Track:
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIDS
    external_urls: ExternalUrls
    href: str
    id: str
    is_local: bool
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: TrackType
    uri: str

    def __init__(self, album: Album, artists: List[Artist], available_markets: List[str], disc_number: int, duration_ms: int, explicit: bool, external_ids: ExternalIDS, external_urls: ExternalUrls, href: str, id: str, is_local: bool, name: str, popularity: int, preview_url: str, track_number: int, type: TrackType, uri: str) -> None:
        self.album = album
        self.artists = artists
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.is_local = is_local
        self.name = name
        self.popularity = popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = type
        self.uri = uri


class Item:
    track: Track
    played_at: datetime
    context: None

    def __init__(self, track: Track, played_at: datetime, context: None) -> None:
        self.track = track
        self.played_at = played_at
        self.context = context


class Welcome2:
    next: str
    cursors: Cursors
    href: str
    items: List[Item]
    limit: int
    offset: int
    previous: str
    total: int

    def __init__(self, href: str, items: List[Item], limit: int, next: str, previous: str = "", total: int = 0, offset: int = 0,cursors: Cursors = None) -> None:
        self.href = href
        self.items = items
        self.limit = limit
        self.next = next
        self.offset = offset
        self.previous = previous
        self.total = total
        self.cursors = cursors
