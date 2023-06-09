class Event:
    """The :class:`Event <Event>` object, which contains an event's details."""

    __attrs__ = [
        "id",
        "fancy_id",
        "name",
        "description",
        "location_type",
        "city",
        "country",
        "channel",
        "platform",
        "event_url",
        "image_url",
        "animation_url",
        "year",
        "start_date",
        "end_date",
        "expiry_date",
        "timezone",
        "from_admin",
        "virtual_event",
        "event_template_id",
        "private_event",
    ]

    def __init__(
        self,
        id,
        fancy_id,
        name,
        description,
        location_type,
        city,
        country,
        channel,
        platform,
        event_url,
        image_url,
        animation_url,
        year,
        start_date,
        end_date,
        expiry_date,
        timezone,
        from_admin,
        virtual_event,
        event_template_id,
        private_event,
    ):
        self.id = id
        self.fancy_id = fancy_id
        self.name = name
        self.description = description
        self.location_type = location_type
        self.city = city
        self.country = country
        self.channel = channel
        self.platform = platform
        self.event_url = event_url
        self.image_url = image_url
        self.animation_url = animation_url
        self.year = year
        self.start_date = start_date
        self.end_date = end_date
        self.expiry_date = expiry_date
        self.timezone = timezone
        self.from_admin = from_admin
        self.virtual_event = virtual_event
        self.event_template_id = event_template_id
        self.private_event = private_event
